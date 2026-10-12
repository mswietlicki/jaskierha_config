/* Jaskier dashboard cards: cached place names and past-week trip history. */
(() => {
  const DAY = 86400000;
  const REFRESH = 300000;
  const CACHE_KEY = "jaskier-place-cache-v1";
  const el = (tag, text, cls) => {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = text;
    if (cls) node.className = cls;
    return node;
  };
  const css = `
    :host { display:block; }
    ha-card { height:100%; box-sizing:border-box; }
    .content { padding:16px; }
    .title { font-size:18px; font-weight:500; margin:0 0 8px; }
    .muted { color:var(--secondary-text-color); font-size:13px; }
    a { color:var(--primary-color); text-decoration:none; }
    a:hover { text-decoration:underline; }
    button { color:var(--primary-text-color); background:var(--secondary-background-color); border:1px solid var(--divider-color); border-radius:8px; min-height:36px; padding:0 12px; cursor:pointer; }
    button:disabled { opacity:.4; cursor:default; }
    .nav { display:flex; align-items:center; gap:8px; margin:12px 0; }
    .range { flex:1; text-align:center; font-weight:500; }
    .events { max-height:420px; overflow:auto; }
    .day { margin:14px 0 4px; font-size:14px; color:var(--secondary-text-color); }
    details { padding:10px 0; border-bottom:1px solid var(--divider-color); }
    summary { cursor:pointer; }
    .times { padding:4px 0 0 16px; font-size:13px; color:var(--secondary-text-color); }
    .description { white-space:pre-wrap; overflow-wrap:anywhere; margin:10px 0; font-size:13px; }
    .place { font-size:18px; line-height:1.5; overflow-wrap:anywhere; }
    .footer { margin-top:12px; display:flex; gap:12px; flex-wrap:wrap; }
  `;
  function setup(card) {
    card.attachShadow({ mode: "open" });
    const style = el("style", css);
    const frame = el("ha-card");
    const content = el("div", undefined, "content");
    frame.append(content);
    card.shadowRoot.append(style, frame);
    card._content = content;
  }
  function km(a, b) {
    const r = Math.PI / 180;
    const x = Math.sin((b.lat-a.lat)*r/2)**2 + Math.cos(a.lat*r)*Math.cos(b.lat*r)*Math.sin((b.lon-a.lon)*r/2)**2;
    return 12742 * Math.asin(Math.sqrt(Math.min(1, Math.max(0, x))));
  }
  function dayParts(date, zone) {
    return Object.fromEntries(new Intl.DateTimeFormat("en-CA", { timeZone:zone, year:"numeric", month:"2-digit", day:"2-digit" }).formatToParts(date).map(p => [p.type,p.value]));
  }
  function dateShift(parts, days) {
    return new Date(Date.UTC(+parts.year,+parts.month-1,+parts.day+days)).toISOString().slice(0,10);
  }
  function midnight(iso, zone) {
    const [y,m,d] = iso.split("-").map(Number);
    const target = Date.UTC(y,m-1,d);
    let value = target;
    const formatter = new Intl.DateTimeFormat("en-CA", { timeZone:zone, year:"numeric", month:"2-digit", day:"2-digit", hour:"2-digit", minute:"2-digit", second:"2-digit", hourCycle:"h23" });
    for (let i=0;i<3;i++) {
      const p = Object.fromEntries(formatter.formatToParts(new Date(value)).map(p=>[p.type,p.value]));
      value += target-Date.UTC(+p.year,+p.month-1,+p.day,+p.hour,+p.minute,+p.second);
    }
    return new Date(value);
  }
  function weekRange(now, offset, zone) {
    const p = dayParts(now, zone);
    return { start:midnight(dateShift(p,offset*7-6),zone), end:midnight(dateShift(p,offset*7+1),zone) };
  }
  function eventTime(event, key) {
    const value = event[key];
    return new Date(typeof value === "string" ? value : value?.dateTime || value?.date);
  }
  function routeUrl(description) {
    const raw = String(description || "").match(/^Route:\s*(https:\/\/\S+)/m)?.[1];
    if (!raw || raw.includes("Unknown")) return null;
    try {
      const url = new URL(raw);
      return url.protocol === "https:" && ["www.google.com","maps.google.com"].includes(url.hostname) ? url.href : null;
    } catch { return null; }
  }

  class JaskierCurrentPlace extends HTMLElement {
    constructor() {
      super(); setup(this); this._attempt=0; this._cache={};
      try { const cache=JSON.parse(localStorage.getItem(CACHE_KEY)||"{}"); if (cache && typeof cache==="object" && !Array.isArray(cache)) this._cache=cache; } catch {}
    }
    setConfig(config) { this._config={ entity:"device_tracker.ewd108_slave_16_gps", ...config }; }
    getCardSize() { return 2; }
    connectedCallback() { this._timer=setInterval(()=>this._update(),60000); this._update(); }
    disconnectedCallback() { clearInterval(this._timer); this._abort?.abort(); }
    set hass(hass) { this._hass=hass; this._update(); }
    _point() {
      const s=this._hass?.states[this._config?.entity];
      const lat=s?.attributes.latitude, lon=s?.attributes.longitude;
      return s && !["unknown","unavailable"].includes(s.state) && Number.isFinite(lat) && Number.isFinite(lon) ? {lat,lon} : null;
    }
    async _update() {
      if (!this._config || !this._hass) return;
      const p=this._point();
      if (!p) { this._render(null); return; }
      const cached=Object.values(this._cache).find(c=>c && typeof c.label==="string" && Number.isFinite(c.lat) && Number.isFinite(c.lon) && Date.now()-c.at<30*DAY && km(p,c)<1);
      if (cached) this._place=cached;
      this._render(p);
      if (!this.isConnected || this._pending || cached || Date.now()-this._attempt<REFRESH) return;
      this._attempt=Date.now(); this._pending=true; this._abort=new AbortController();
      const timer=setTimeout(()=>this._abort.abort(),15000);
      try {
        const url=new URL(this._config.geocoder_url || "https://photon.komoot.io/reverse");
        url.search=new URLSearchParams({lat:p.lat.toFixed(4),lon:p.lon.toFixed(4),limit:"1"}).toString();
        const response=await fetch(url, {signal:this._abort.signal, referrerPolicy:"no-referrer"});
        if (!response.ok) throw new Error("Place lookup unavailable");
        const data=await response.json(), props=data.features?.[0]?.properties;
        if (!props) throw new Error("No place found");
        const label=[...new Set([props.name||[props.street,props.housenumber].filter(Boolean).join(" "),props.city||props.district,props.state,props.country].filter(v=>typeof v==="string" && v))].join(", ");
        if (!label) throw new Error("No place name");
        this._place={...p,label,at:Date.now()};
        this._cache[`${p.lat.toFixed(3)},${p.lon.toFixed(3)}`]=this._place;
        this._cache=Object.fromEntries(Object.entries(this._cache).sort((a,b)=>b[1].at-a[1].at).slice(0,100));
        try { localStorage.setItem(CACHE_KEY,JSON.stringify(this._cache)); } catch {}
        this._render(this._point());
      } catch {
        this._render(this._point(),true);
      } finally { clearTimeout(timer); this._pending=false; }
    }
    _render(p, failed=false) {
      this._content.replaceChildren(el("h3",this._config?.title||"Current location","title"));
      const current=p && this._place && km(p,this._place)<1;
      this._content.append(el("div",!p?"GPS temporarily unavailable":current?`Near ${this._place.label}`:failed?"Place description unavailable":"Finding place description…","place"));
      if (!p) return;
      this._content.append(el("div",`${p.lat.toFixed(4)}, ${p.lon.toFixed(4)}`,"muted"));
      const footer=el("div",undefined,"footer muted");
      const map=el("a","Open this place"); map.href=`https://www.openstreetmap.org/?mlat=${p.lat}&mlon=${p.lon}#map=15/${p.lat}/${p.lon}`; map.target="_blank"; map.rel="noopener noreferrer";
      const attribution=el("a","Place data: OpenStreetMap / Photon"); attribution.href="https://www.openstreetmap.org/copyright"; attribution.target="_blank"; attribution.rel="noopener noreferrer";
      footer.append(map,attribution); this._content.append(footer);
    }
  }

  class JaskierWeeklyTrips extends HTMLElement {
    constructor() { super(); setup(this); this._offset=0; this._events=[]; this._loaded=0; this._sequence=0; }
    setConfig(config) { if (!config.entity) throw new Error("A trip calendar is required"); this._config=config; }
    getCardSize() { return 6; }
    connectedCallback() { this._timer=setInterval(()=>this._load(),REFRESH); this._load(); }
    disconnectedCallback() { clearInterval(this._timer); this._sequence++; this._pending=null; this._loaded=0; }
    set hass(hass) {
      const signature=hass.states[this._config?.entity]?.last_updated;
      if (signature!==this._signature) { this._loaded=0; this._signature=signature; }
      this._hass=hass; this._load();
    }
    async _load(force=false) {
      if (!this.isConnected || !this._hass || !this._config) return;
      this._zone=this._hass.config.time_zone||"Europe/Warsaw";
      this._range=weekRange(new Date(),this._offset,this._zone);
      const key=`${this._range.start.toISOString()}/${this._range.end.toISOString()}`;
      if (this._pending===key || (!force && this._key===key && Date.now()-this._loaded<REFRESH)) return;
      const request=++this._sequence; this._pending=key; this._key=key; this._loaded=Date.now(); this._events=[]; this._render(true);
      try {
        const query=new URLSearchParams({start:this._range.start.toISOString(),end:this._range.end.toISOString()});
        const events=await this._hass.callApi("GET",`calendars/${this._config.entity}?${query}`);
        if (request!==this._sequence) return;
        this._events=(Array.isArray(events)?events:[]).filter(e=>Number.isFinite(eventTime(e,"start").getTime())).sort((a,b)=>eventTime(b,"start")-eventTime(a,"start"));
        this._render(false);
      } catch { if (request===this._sequence) this._render(false,true); }
      finally { if (request===this._sequence) this._pending=null; }
    }
    _render(loading=false,failed=false) {
      const locale=this._hass.locale?.language||"en-GB", zone=this._zone;
      const date=new Intl.DateTimeFormat(locale,{timeZone:zone,day:"numeric",month:"short"});
      const weekday=new Intl.DateTimeFormat(locale,{timeZone:zone,weekday:"long",day:"numeric",month:"short"});
      const time=new Intl.DateTimeFormat(locale,{timeZone:zone,hour:"2-digit",minute:"2-digit"});
      this._content.replaceChildren(el("h3",this._config.title||"Trips · last 7 days","title"));
      const nav=el("div",undefined,"nav"), previous=el("button","‹"), next=el("button","›"), latest=el("button","Latest");
      previous.title="Previous seven days"; next.title="Next seven days";
      previous.onclick=()=>{this._offset--;this._load(true);}; next.onclick=()=>{this._offset++;this._load(true);}; next.disabled=this._offset===0;
      latest.onclick=()=>{this._offset=0;this._load(true);};
      nav.append(previous,el("div",`${date.format(this._range.start)} – ${date.format(new Date(this._range.end.getTime()-1))}`,"range"),next,latest); this._content.append(nav);
      const total=this._events.reduce((n,e)=>n+Number(String(e.description||e.summary).match(/(?:Distance:|—)\s*([\d.]+)\s*km/)?.[1]||0),0);
      this._content.append(el("div",loading?"Loading trips…":failed?"Trip history unavailable. Try again shortly.":`${this._events.length} trips · ${total.toLocaleString(locale,{maximumFractionDigits:1})} km`,"muted"));
      const list=el("div",undefined,"events"); let group="";
      for (const event of this._events) {
        const start=eventTime(event,"start"), end=eventTime(event,"end"), day=weekday.format(start);
        if (day!==group) { list.append(el("h4",day,"day")); group=day; }
        const item=el("details"), summary=el("summary",event.summary||"Trip");
        item.append(summary,el("div",`${time.format(start)} – ${Number.isFinite(end.getTime())?time.format(end):""}${Number.isFinite(end.getTime())?` · ${Math.max(0,Math.round((end-start)/60000))} min`:""}`,"times"));
        if (event.description) item.append(el("div",String(event.description).replace(/^Route:.*$/m,"").trim(),"description"));
        const url=routeUrl(event.description);
        if (url) { const route=el("a","View recorded route"); route.href=url; route.target="_blank"; route.rel="noopener noreferrer"; item.append(route); }
        list.append(item);
      }
      if (!loading && !failed && !this._events.length) list.append(el("p","No completed trips in these seven days.","muted"));
      this._content.append(list);
    }
  }
  if (!customElements.get("jaskier-current-place")) customElements.define("jaskier-current-place",JaskierCurrentPlace);
  if (!customElements.get("jaskier-weekly-trips")) customElements.define("jaskier-weekly-trips",JaskierWeeklyTrips);
  window.customCards=window.customCards||[];
  window.customCards.push({type:"jaskier-current-place",name:"Jaskier current place",description:"Cached GPS place description"},{type:"jaskier-weekly-trips",name:"Jaskier weekly trips",description:"Completed trips in the past seven days"});
  window.JaskierTripsUtils={weekRange,routeUrl,eventTime,km};
})();
