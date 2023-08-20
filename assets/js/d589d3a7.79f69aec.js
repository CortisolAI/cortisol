"use strict";(self.webpackChunkcortisol=self.webpackChunkcortisol||[]).push([[162],{3905:(e,t,o)=>{o.d(t,{Zo:()=>c,kt:()=>h});var n=o(7294);function i(e,t,o){return t in e?Object.defineProperty(e,t,{value:o,enumerable:!0,configurable:!0,writable:!0}):e[t]=o,e}function l(e,t){var o=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),o.push.apply(o,n)}return o}function r(e){for(var t=1;t<arguments.length;t++){var o=null!=arguments[t]?arguments[t]:{};t%2?l(Object(o),!0).forEach((function(t){i(e,t,o[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(o)):l(Object(o)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(o,t))}))}return e}function a(e,t){if(null==e)return{};var o,n,i=function(e,t){if(null==e)return{};var o,n,i={},l=Object.keys(e);for(n=0;n<l.length;n++)o=l[n],t.indexOf(o)>=0||(i[o]=e[o]);return i}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(n=0;n<l.length;n++)o=l[n],t.indexOf(o)>=0||Object.prototype.propertyIsEnumerable.call(e,o)&&(i[o]=e[o])}return i}var s=n.createContext({}),p=function(e){var t=n.useContext(s),o=t;return e&&(o="function"==typeof e?e(t):r(r({},t),e)),o},c=function(e){var t=p(e.components);return n.createElement(s.Provider,{value:t},e.children)},u="mdxType",m={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},d=n.forwardRef((function(e,t){var o=e.components,i=e.mdxType,l=e.originalType,s=e.parentName,c=a(e,["components","mdxType","originalType","parentName"]),u=p(o),d=i,h=u["".concat(s,".").concat(d)]||u[d]||m[d]||l;return o?n.createElement(h,r(r({ref:t},c),{},{components:o})):n.createElement(h,r({ref:t},c))}));function h(e,t){var o=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var l=o.length,r=new Array(l);r[0]=d;var a={};for(var s in t)hasOwnProperty.call(t,s)&&(a[s]=t[s]);a.originalType=e,a[u]="string"==typeof e?e:i,r[1]=a;for(var p=2;p<l;p++)r[p]=o[p];return n.createElement.apply(null,r)}return n.createElement.apply(null,o)}d.displayName="MDXCreateElement"},9390:(e,t,o)=>{o.r(t),o.d(t,{assets:()=>s,contentTitle:()=>r,default:()=>m,frontMatter:()=>l,metadata:()=>a,toc:()=>p});var n=o(7462),i=(o(7294),o(3905));const l={title:"Getting Started",sidebar_position:2},r=void 0,a={unversionedId:"getting-started",id:"getting-started",title:"Getting Started",description:"Installation",source:"@site/docs/getting-started.md",sourceDirName:".",slug:"/getting-started",permalink:"/cortisol/getting-started",draft:!1,editUrl:"https://github.com/CortisolAI/cortisol/docs/docs/getting-started.md",tags:[],version:"current",sidebarPosition:2,frontMatter:{title:"Getting Started",sidebar_position:2},sidebar:"tutorialSidebar",previous:{title:"What is Cortisol?",permalink:"/cortisol/"},next:{title:"Writing a cortisolfile",permalink:"/cortisol/writing-a-cortisolfile"}},s={},p=[{value:"Installation",id:"installation",level:2},{value:"Prerequisities",id:"prerequisities",level:3},{value:"Install Cortisol",id:"install-cortisol",level:3},{value:"Your first log cost estimation",id:"your-first-log-cost-estimation",level:2},{value:"Your first log cost estimation with Docker",id:"your-first-log-cost-estimation-with-docker",level:2}],c={toc:p},u="wrapper";function m(e){let{components:t,...l}=e;return(0,i.kt)(u,(0,n.Z)({},c,l,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h2",{id:"installation"},"Installation"),(0,i.kt)("h3",{id:"prerequisities"},"Prerequisities"),(0,i.kt)("p",null,"Cortisol requires the following one of the following Python versions: 3.8, 3.9, 3.10 or 3.11"),(0,i.kt)("h3",{id:"install-cortisol"},"Install Cortisol"),(0,i.kt)("p",null,"At the command line:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"pip install cortisol\n")),(0,i.kt)("h2",{id:"your-first-log-cost-estimation"},"Your first log cost estimation"),(0,i.kt)("p",null,"Let's dive right in and get our hands dirty with Cortisol! As an integral part of your software development workflow, Cortisol CLI brings predictability to managing log costs. "),(0,i.kt)("p",null,"First things first! We need a RESTful service and so you'll need to do the following steps:"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},"Clone this example repo ",(0,i.kt)("a",{parentName:"li",href:"https://github.com/CortisolAI/getting-started-example"},"https://github.com/CortisolAI/getting-started-example")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("inlineCode",{parentName:"li"},"cd getting-started-example")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("inlineCode",{parentName:"li"},"mkvirtualenv getting-started-cortisol")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("inlineCode",{parentName:"li"},"python -m app.main")," which will make the service available at ",(0,i.kt)("inlineCode",{parentName:"li"},"http://127.0.0.1:8080/"))),(0,i.kt)("p",null,"And, now, it's time to create your first cortisol file. Copy and paste the following in a file named ",(0,i.kt)("inlineCode",{parentName:"p"},"cortisolfile.py")," in the root path of getting-started-example repo:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},'from locust import task\n\nfrom cortisol.cortisollib.users import CortisolHttpUser\n\n\nclass WebsiteUser(CortisolHttpUser):\n    @task\n    def my_task(self):\n        self.client.get("/")\n\n')),(0,i.kt)("p",null,"Here we define a class for the users that we will be simulating. It must always inherit from ",(0,i.kt)("inlineCode",{parentName:"p"},"CortisolHttpUser <cortisollib.users.CortisolHttpUser>"),"."),(0,i.kt)("p",null,"We've declared 1 task by decorating two methods with ",(0,i.kt)("inlineCode",{parentName:"p"},"@task"),". The ",(0,i.kt)("inlineCode",{parentName:"p"},"my_task")," method calls the root path of the restful service that just returns a simple JSON response."),(0,i.kt)("p",null,"You can define multiple tasks for each resource of your web service."),(0,i.kt)("p",null,"Almost there! It's time to run the cortisol command and get your first log cost estimates. Before we do that, make sure you know the root path of where the getting-started-example repo is located. For illustration purposes, let's assume the path is ",(0,i.kt)("inlineCode",{parentName:"p"},"/some/path/getting-started-example/"),"."),(0,i.kt)("p",null,"Switch to another terminal window, enable the ",(0,i.kt)("inlineCode",{parentName:"p"},"getting-started-cortisol")," virtual env and run the following command in the terminal:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-terminal"},"cortisol logs cost-estimate --host http://127.0.0.1:8080 --users 10 --spawn-rate 5 --run-time 10s --cortisol-file cortisolfile.py --log-file cortisol_app.log\n")),(0,i.kt)("p",null,"You'll get some results after 10 seconds that look like these ones:"),(0,i.kt)("p",null,(0,i.kt)("img",{alt:"Cortisol",src:o(9745).Z,width:"643",height:"373"})),(0,i.kt)("p",null,"Before we dive into the results, let's understand what load testing ran in the background in order to receive the latter log cost estimates."),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"--host http://127.0.0.1:8080")," the FAST API runs at ",(0,i.kt)("inlineCode",{parentName:"li"},"http://127.0.0.1:8080")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"--users 10")," The peak number of concurrent users is 10"),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"--spawn-rate 5")," Spawn 5 users per second"),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"--run-time 10s")," Stop after 10 seconds"),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"--cortisol-file cortisolfile.py")," path to cortisolfile"),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"--log-file cortisol_app.log")," path to where logs are saved")),(0,i.kt)("p",null,"Let's get back to the results. The total log volume per month of running this FAST API with the defined user behaviour in the cortisolfile and in the cortisol command arguments is going to be available at the top of the table. The log costs per observability tool are per month and are explained below:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"Datadog: 30 day log retention and billed annually"),(0,i.kt)("li",{parentName:"ul"},"Grafana: Cloud Pro plan is chosen"),(0,i.kt)("li",{parentName:"ul"},"New Relic: Pro plan is chosen"),(0,i.kt)("li",{parentName:"ul"},"GCP Cloud Logging: based on the pricing on their website")),(0,i.kt)("p",null,"Please, note that free tiers have been included to all the costs above"),(0,i.kt)("h2",{id:"your-first-log-cost-estimation-with-docker"},"Your first log cost estimation with Docker"),(0,i.kt)("p",null,"Let's do the same but run the FAST API in a Docker container."),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},"Clone this example repo ",(0,i.kt)("a",{parentName:"li",href:"https://github.com/CortisolAI/getting-started-example"},"https://github.com/CortisolAI/getting-started-example")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("inlineCode",{parentName:"li"},"cd getting-started-example")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("inlineCode",{parentName:"li"},"make build")," to build the Docker image"),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("inlineCode",{parentName:"li"},"make run")," to run the container. The printed container ID is important. This command will make the service available at ",(0,i.kt)("inlineCode",{parentName:"li"},"http://127.0.0.1:8080/"))),(0,i.kt)("p",null,"On another terminal window:"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},"Create a virtualenv ",(0,i.kt)("inlineCode",{parentName:"li"},"mkvirtualenv getting-started-cortisol")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("inlineCode",{parentName:"li"},"pip install cortisol"))),(0,i.kt)("p",null,"You will need to pass the container ID, and just define the log file name. No need to pass the entire path to the log file:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-terminal"},"cortisol logs cost-estimate --host http://127.0.0.1:8080 --users 10 --spawn-rate 5 --run-time 10s --cortisol-file cortisolfile.py --container-id d3a45b9e27ca03b52d2fe9d4c7c55f8254829555c96c6b79bc950caaf33719f8 --cortisol-file ./examples/cortisolfile.py --log-file cortisol_app.log\n")),(0,i.kt)("p",null,"And, you'll get some results in 10 seconds."),(0,i.kt)("p",null,"Make sure to run ",(0,i.kt)("inlineCode",{parentName:"p"},"make stop")," and ",(0,i.kt)("inlineCode",{parentName:"p"},"make clean")," to stop/delete the Docker image and container."))}m.isMDXComponent=!0},9745:(e,t,o)=>{o.d(t,{Z:()=>n});const n=o.p+"assets/images/getting-started-results-bdbefa5b4f504bc0b9ace959b063c20e.png"}}]);