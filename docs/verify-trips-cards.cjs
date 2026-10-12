const fs = require('fs');
const vm = require('vm');
const assert = require('assert/strict');
class Element {
  constructor() { this.children=[]; this.isConnected=true; this.textContent=''; }
  append(...nodes) { this.children.push(...nodes); }
  replaceChildren(...nodes) { this.children=nodes; }
  attachShadow() { return this.shadowRoot=new Element(); }
}
global.HTMLElement=Element;
global.document={createElement:()=>new Element()};
global.window={};
const registry=new Map();
global.customElements={get:n=>registry.get(n),define:(n,c)=>registry.set(n,c)};
const storage=new Map();
global.localStorage={getItem:n=>storage.get(n),setItem:(n,v)=>storage.set(n,v)};
vm.runInThisContext(fs.readFileSync('www/jaskier-trips-cards.js','utf8'));
const {weekRange,routeUrl}=window.JaskierTripsUtils;
const fall=weekRange(new Date('2026-10-26T12:00:00Z'),0,'Europe/Warsaw');
assert.equal(fall.start.toISOString(),'2026-10-19T22:00:00.000Z');
assert.equal(fall.end.toISOString(),'2026-10-26T23:00:00.000Z');
assert.equal((fall.end-fall.start)/3600000,169);
const spring=weekRange(new Date('2026-03-30T12:00:00Z'),0,'Europe/Warsaw');
assert.equal((spring.end-spring.start)/3600000,167);
assert.equal(routeUrl('Route: https://example.com/attack'),null);
assert.equal(routeUrl('Route: https://www.google.com/maps/dir/?destination=Unknown'),null);
const text=e=>[e.textContent,...e.children.map(text)].join(' ');
const settle=()=>new Promise(r=>setImmediate(r));
(async()=>{
  const fixture=JSON.parse(fs.readFileSync('docs/trips-week-fixture.json','utf8'));
  let calendarCalls=0;
  const hass={config:{time_zone:'Europe/Warsaw'},locale:{language:'en-GB'},states:{'calendar.jaskier_trips':{last_updated:'2026-10-12T08:00:00Z'}},callApi:async()=>{calendarCalls++;return fixture.map(e=>({...e,start:{dateTime:e.start},end:{dateTime:e.end}}));}};
  const trips=new (registry.get('jaskier-weekly-trips'))();
  trips.setConfig({entity:'calendar.jaskier_trips'});trips.hass=hass;await settle();
  assert.ok(text(trips.shadowRoot).includes('9 trips · 112 km'));
  assert.ok(text(trips.shadowRoot).includes('8 Oct'));
  trips.hass=hass;await settle();assert.equal(calendarCalls,1);
  trips.disconnectedCallback();trips.hass=hass;await settle();assert.equal(calendarCalls,2);
  let lookups=0;
  global.fetch=async()=>{lookups++;return {ok:true,json:async()=>({features:[{properties:{name:'Kwiatowa',city:'Michałów-Reginów',country:'Polska'}}]})};};
  const place=new (registry.get('jaskier-current-place'))();place.setConfig({});
  const gps={'device_tracker.ewd108_slave_16_gps':{state:'home',attributes:{latitude:52.4282,longitude:20.9774}}};
  place.hass={states:gps};await settle();
  assert.ok(text(place.shadowRoot).includes('Michałów-Reginów'));
  place.hass={states:gps};await settle();assert.equal(lookups,1);
  place.hass={states:{'device_tracker.ewd108_slave_16_gps':{state:'unavailable',attributes:{}}}};await settle();
  assert.ok(text(place.shadowRoot).includes('GPS temporarily unavailable'));
  assert.equal(lookups,1);
  console.log('Verified seven-day ranges, DST changes, nine recorded trips, route URL safety, refresh caching, and unavailable GPS handling.');
})().catch(e=>{console.error(e);process.exitCode=1;});
