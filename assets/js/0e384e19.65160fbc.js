"use strict";(self.webpackChunkcortisol=self.webpackChunkcortisol||[]).push([[671],{3905:(e,t,o)=>{o.d(t,{Zo:()=>p,kt:()=>m});var r=o(7294);function n(e,t,o){return t in e?Object.defineProperty(e,t,{value:o,enumerable:!0,configurable:!0,writable:!0}):e[t]=o,e}function i(e,t){var o=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),o.push.apply(o,r)}return o}function a(e){for(var t=1;t<arguments.length;t++){var o=null!=arguments[t]?arguments[t]:{};t%2?i(Object(o),!0).forEach((function(t){n(e,t,o[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(o)):i(Object(o)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(o,t))}))}return e}function s(e,t){if(null==e)return{};var o,r,n=function(e,t){if(null==e)return{};var o,r,n={},i=Object.keys(e);for(r=0;r<i.length;r++)o=i[r],t.indexOf(o)>=0||(n[o]=e[o]);return n}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)o=i[r],t.indexOf(o)>=0||Object.prototype.propertyIsEnumerable.call(e,o)&&(n[o]=e[o])}return n}var l=r.createContext({}),c=function(e){var t=r.useContext(l),o=t;return e&&(o="function"==typeof e?e(t):a(a({},t),e)),o},p=function(e){var t=c(e.components);return r.createElement(l.Provider,{value:t},e.children)},u="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},h=r.forwardRef((function(e,t){var o=e.components,n=e.mdxType,i=e.originalType,l=e.parentName,p=s(e,["components","mdxType","originalType","parentName"]),u=c(o),h=n,m=u["".concat(l,".").concat(h)]||u[h]||d[h]||i;return o?r.createElement(m,a(a({ref:t},p),{},{components:o})):r.createElement(m,a({ref:t},p))}));function m(e,t){var o=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var i=o.length,a=new Array(i);a[0]=h;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s[u]="string"==typeof e?e:n,a[1]=s;for(var c=2;c<i;c++)a[c]=o[c];return r.createElement.apply(null,a)}return r.createElement.apply(null,o)}h.displayName="MDXCreateElement"},9881:(e,t,o)=>{o.r(t),o.d(t,{assets:()=>l,contentTitle:()=>a,default:()=>d,frontMatter:()=>i,metadata:()=>s,toc:()=>c});var r=o(7462),n=(o(7294),o(3905));const i={slug:"/",title:"What is Cortisol?",sidebar_position:1},a="Cortisol",s={unversionedId:"intro",id:"intro",title:"What is Cortisol?",description:"Cortisol",source:"@site/docs/intro.md",sourceDirName:".",slug:"/",permalink:"/cortisol/",draft:!1,editUrl:"https://github.com/CortisolAI/cortisol/docs/docs/intro.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{slug:"/",title:"What is Cortisol?",sidebar_position:1},sidebar:"tutorialSidebar",next:{title:"Getting Started",permalink:"/cortisol/getting-started"}},l={},c=[{value:"What is Cortisol?",id:"what-is-cortisol",level:2},{value:"How does it work?",id:"how-does-it-work",level:3},{value:"Name &amp; Background",id:"name--background",level:3},{value:"Authors",id:"authors",level:3}],p={toc:c},u="wrapper";function d(e){let{components:t,...i}=e;return(0,n.kt)(u,(0,r.Z)({},p,i,{components:t,mdxType:"MDXLayout"}),(0,n.kt)("h1",{id:"cortisol"},"Cortisol"),(0,n.kt)("p",null,(0,n.kt)("img",{alt:"Cortisol",src:o(4018).Z,width:"1656",height:"669"})),(0,n.kt)("p",null,"Let's discover ",(0,n.kt)("strong",{parentName:"p"},"Cortisol in less than 5 minutes"),"."),(0,n.kt)("h2",{id:"what-is-cortisol"},"What is Cortisol?"),(0,n.kt)("p",null,"Cortisol is an open-source command-line tool designed specifically for web services. It offers easy-to-use cost estimation and forecasting capabilities tailroed to main observability tools like ",(0,n.kt)("a",{parentName:"p",href:"https://www.datadoghq.com/"},"Datadog"),", ",(0,n.kt)("a",{parentName:"p",href:"https://newrelic.com/"},"New Relic"),", ",(0,n.kt)("a",{parentName:"p",href:"https://grafana.com/"},"Grafana")," and ",(0,n.kt)("a",{parentName:"p",href:"https://cloud.google.com/logging"},"GCP Cloud Logging"),". Cortisol assists users in planning and optimizing their log costs before deploying their web services. It operates on a foundation inspired by ",(0,n.kt)("a",{parentName:"p",href:"https://locust.io/"},"Locust"),", allowing users to define user behavior using a regular Python script \ud83d\udcb0\ud83d\udcc9."),(0,n.kt)("h3",{id:"how-does-it-work"},"How does it work?"),(0,n.kt)("p",null,"Cortisol seamlessly harnesses the power of ",(0,n.kt)("a",{parentName:"p",href:"https://locust.io/"},"Locust")," for load testing. Users simply provide a standard Python script that outlines the anticipated user behavior on their web service. Cortisol, in turn, processes the load test's log file to project monthly log costs. It achieves this by referencing the public pricing figures of ",(0,n.kt)("a",{parentName:"p",href:"https://www.datadoghq.com/"},"Datadog"),", ",(0,n.kt)("a",{parentName:"p",href:"https://newrelic.com/"},"New Relic"),", ",(0,n.kt)("a",{parentName:"p",href:"https://grafana.com/"},"Grafana")," and ",(0,n.kt)("a",{parentName:"p",href:"https://cloud.google.com/logging"},"GCP Cloud Logging"),"."),(0,n.kt)("h3",{id:"name--background"},"Name & Background"),(0,n.kt)("p",null,'Picture this: the world of observability is brimming with fantastic tools like Grafana, Datadog, and New Relic. But here\'s the catch \u2013 costs can sneak up on you, catching you off guard or, worse, too late. And don\'t get us started on those log costs; they can go from "too little" to "what?!" in no time, even for the simplest web services. We wanted a tool that\'s right there in the thick of your software development workflow, because programming should always be a joyful ride.'),(0,n.kt)("p",null,"In Cortisol, you define the behaviour of your users using Python code, much like you would in load testing scenarios. Various load testing scenarios result in logs of different sizes, leading to differing costs. Having this information beforehand can assist you in more effective budgeting and, potentially, in eliminating unnecessary log statements from your code."),(0,n.kt)("p",null,"Cortisol takes its name from the steroid hormone that helps our bodies respond to stress by increasing alertness, boosting energy, and regulating metabolism. It also plays a role in controlling blood sugar levels, reducing inflammation, and supporting the immune system. "),(0,n.kt)("h3",{id:"authors"},"Authors"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},"Dionysis Varelas (",(0,n.kt)("a",{parentName:"li",href:"https://github.com/dvarelas"},"@dvarelas")," on Github)"),(0,n.kt)("li",{parentName:"ul"},"Pavlos Mitsoulis (",(0,n.kt)("a",{parentName:"li",href:"https://github.com/pm3310"},"@pm330")," on Github)"),(0,n.kt)("li",{parentName:"ul"},"Narek Verdian (",(0,n.kt)("a",{parentName:"li",href:"https://www.linkedin.com/in/narek/"},"@narek")," on LinkedIn)")))}d.isMDXComponent=!0},4018:(e,t,o)=>{o.d(t,{Z:()=>r});const r=o.p+"assets/images/cortisol_h_large-adf5e507f801b148da4966597bf1c695.png"}}]);