"use strict";(self.webpackChunkcortisol=self.webpackChunkcortisol||[]).push([[592],{3905:(e,t,n)=>{n.d(t,{Zo:()=>c,kt:()=>d});var i=n(7294);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function r(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);t&&(i=i.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,i)}return n}function a(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?r(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):r(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,i,o=function(e,t){if(null==e)return{};var n,i,o={},r=Object.keys(e);for(i=0;i<r.length;i++)n=r[i],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(i=0;i<r.length;i++)n=r[i],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var l=i.createContext({}),p=function(e){var t=i.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):a(a({},t),e)),n},c=function(e){var t=p(e.components);return i.createElement(l.Provider,{value:t},e.children)},u="mdxType",m={inlineCode:"code",wrapper:function(e){var t=e.children;return i.createElement(i.Fragment,{},t)}},h=i.forwardRef((function(e,t){var n=e.components,o=e.mdxType,r=e.originalType,l=e.parentName,c=s(e,["components","mdxType","originalType","parentName"]),u=p(n),h=o,d=u["".concat(l,".").concat(h)]||u[h]||m[h]||r;return n?i.createElement(d,a(a({ref:t},c),{},{components:n})):i.createElement(d,a({ref:t},c))}));function d(e,t){var n=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var r=n.length,a=new Array(r);a[0]=h;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s[u]="string"==typeof e?e:o,a[1]=s;for(var p=2;p<r;p++)a[p]=n[p];return i.createElement.apply(null,a)}return i.createElement.apply(null,n)}h.displayName="MDXCreateElement"},5017:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>l,contentTitle:()=>a,default:()=>m,frontMatter:()=>r,metadata:()=>s,toc:()=>p});var i=n(7462),o=(n(7294),n(3905));const r={title:"Continuous Integration Visibility",sidebar_position:6},a=void 0,s={unversionedId:"CI-visibility",id:"CI-visibility",title:"Continuous Integration Visibility",description:"Continuous Integration Visibility",source:"@site/docs/CI-visibility.md",sourceDirName:".",slug:"/CI-visibility",permalink:"/cortisol/CI-visibility",draft:!1,editUrl:"https://github.com/CortisolAI/cortisol/docs/docs/CI-visibility.md",tags:[],version:"current",sidebarPosition:6,frontMatter:{title:"Continuous Integration Visibility",sidebar_position:6},sidebar:"tutorialSidebar",previous:{title:"Best practices",permalink:"/cortisol/best-practices"},next:{title:"How-to guides",permalink:"/cortisol/how-tos"}},l={},p=[{value:"Continuous Integration Visibility",id:"continuous-integration-visibility",level:2},{value:"Cortisol as a Github Action",id:"cortisol-as-a-github-action",level:2}],c={toc:p},u="wrapper";function m(e){let{components:t,...r}=e;return(0,o.kt)(u,(0,i.Z)({},c,r,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h2",{id:"continuous-integration-visibility"},"Continuous Integration Visibility"),(0,o.kt)("p",null,"Streamline your CI/CD pipelines with detailed visibility into your expected log costs."),(0,o.kt)("p",null,"There are examples below on how to enable Cortisol in your CI/CD pipeline."),(0,o.kt)("h2",{id:"cortisol-as-a-github-action"},"Cortisol as a Github Action"),(0,o.kt)("p",null,"For more information about Github Action, please refer ",(0,o.kt)("a",{parentName:"p",href:"https://github.com/features/actions"},"here"),"."),(0,o.kt)("p",null,"Let's suppose that you want to run Cortisol as a step in a Github action for this FastAPI ",(0,o.kt)("a",{parentName:"p",href:"https://github.com/CortisolAI/getting-started-example"},"repository"),"."),(0,o.kt)("p",null,"It's very simple! "),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},"Fork this ",(0,o.kt)("a",{parentName:"li",href:"https://github.com/CortisolAI/getting-started-example"},"repository")," "),(0,o.kt)("li",{parentName:"ol"},"Create a file named ",(0,o.kt)("inlineCode",{parentName:"li"},"cortisolfile.py")," at the root of the repository with the following content:")),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-Python"},'from locust import task\n\nfrom cortisol.cortisollib.users import CortisolHttpUser\n\n\nclass WebsiteUser(CortisolHttpUser):\n    @task\n    def my_task(self):\n        self.client.get("/")\n')),(0,o.kt)("ol",{start:3},(0,o.kt)("li",{parentName:"ol"},"Create a file named ",(0,o.kt)("inlineCode",{parentName:"li"},"my_config.yaml")," at the root of the repository with the following content:")),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-YAML"},'host: "http://127.0.0.1:8080"\nlog-file: "cortisol_app.log"\nusers: 10\nspawn-rate: 5\nrun-time: "10s"\ncortisol-file: "cortisolfile.py"\n')),(0,o.kt)("ol",{start:4},(0,o.kt)("li",{parentName:"ol"},"Create in this repository the following path ",(0,o.kt)("inlineCode",{parentName:"li"},".github/workflows/")),(0,o.kt)("li",{parentName:"ol"},"Save under ",(0,o.kt)("inlineCode",{parentName:"li"},".github/workflows/")," a file named ",(0,o.kt)("inlineCode",{parentName:"li"},"main.yml")," with the following content:")),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-YAML"},'name: Main Workflow\n\non:\n  push:\n    branches:\n      - main  # Replace with the branch you want to trigger on\n\njobs:\n  build:\n    runs-on: ubuntu-latest\n\n    steps:\n    - name: Checkout Repository\n      uses: actions/checkout@v2  \n\n    - name: Set up Python  # Replace with your desired programming language.\n      uses: actions/setup-python@v4\n      with:\n        python-version: "3.10"  # Replace with your desired Python version.\n\n    - name: Install Dependencies  # Replace with your desired dependency management tool.\n      run: |\n        pip install -r requirements.txt\n\n    - name: Run FastAPI Server in the background\n      run: |\n        nohup python -m app.main &\n\n    - name: Verify server is running\n      run: |\n        curl http://127.0.0.1:8080\n\n    - name: Cortisol log costs pre-production\n      run: |\n        cortisol logs cost-estimate --config my_config.yaml\n')),(0,o.kt)("ol",{start:6},(0,o.kt)("li",{parentName:"ol"},"Push the code changes to your ",(0,o.kt)("inlineCode",{parentName:"li"},"main")," branch."),(0,o.kt)("li",{parentName:"ol"},"You should see in the Actions tab of your forked repository this action being in progress. Click on it. Once it's finished you should something like that:")),(0,o.kt)("p",null,(0,o.kt)("img",{alt:"GH-Action",src:n(4241).Z,width:"1214",height:"534"})),(0,o.kt)("p",null,"Let's explain the steps in this Github Action workflow:"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"Checkout Repository"),": This step checks out the source code repository into the runner's workspace. It uses the ",(0,o.kt)("inlineCode",{parentName:"li"},"actions/checkout")," action with version ",(0,o.kt)("inlineCode",{parentName:"li"},"v2"),"."),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"Set up Python"),": This step sets up the Python environment on the runner. It specifies the desired Python version, which is version ",(0,o.kt)("inlineCode",{parentName:"li"},"3.10")," in this case."),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"Install Dependencies"),": This step installs Python dependencies from a ",(0,o.kt)("inlineCode",{parentName:"li"},"requirements.txt")," file using the ",(0,o.kt)("inlineCode",{parentName:"li"},"pip")," package manager. The ",(0,o.kt)("inlineCode",{parentName:"li"},"requirements.txt")," file contains the ",(0,o.kt)("inlineCode",{parentName:"li"},"cortisol")," library."),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"Run FastAPI Server in the background"),": This step starts a FastAPI server in the background. The nohup command allows the server to keep running after this step is completed and, more importantly, it doesn't block the entire Github Action."),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"Verify server is running"),": This step uses ",(0,o.kt)("inlineCode",{parentName:"li"},"curl")," to make an HTTP request to the FastAPI server to verify that it is running and responsive."),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"Cortisol log costs pre-production"),": This step runs Cortisol with the arguments ",(0,o.kt)("inlineCode",{parentName:"li"},"logs cost-estimate --config my_config.yaml"),". It estimates log costs pre-production.")))}m.isMDXComponent=!0},4241:(e,t,n)=>{n.d(t,{Z:()=>i});const i=n.p+"assets/images/gh-action-cortisol-5902ae4e3ce2929af2e9843c97b45ed6.png"}}]);