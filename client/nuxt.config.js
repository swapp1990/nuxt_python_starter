export default {
  components: true,
  /*
   ** Headers of the page
   */
  head: {
    title: "Nuxt Starter Project",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      {
        hid: "description",
        name: "description",
        content:
          "Nuxt Starter Project.",
      },
    //   {
    //     name: "google-site-verification",
    //     content: "LtnsnfX3t-Tc1iduoq8d6Up8U2yGgpby2ixOJCt-zgw",
    //   },
    ],
    script: [
		{
			src: 'https://js.stripe.com/v3',
			defer: true
		}
	],
    link: [
    //   { rel: "icon", type: "image/x-icon", href: "/footloose-logo.png" },
      //   {
      //     rel: "stylesheet",
      //     href:
      //       "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons",
      //   },
    ],
  },
  //   fontLoader: {
  //     // Paste a google link here
  //     url:
  //       "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons",

  //     // Enable 'prefetch' and 'preconnect' options
  //     prefetch: true,
  //     preconnect: false,
  //   },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: "#fff" },
  /*
   ** Global CSS
   */
//   css: ["assets/font/roboto.css"],
  /*
   ** Plugins to load before mounting the App
   */
//   plugins: [
//     { src: "~/plugins/vue-carousel-3d.js", mode: "client" },
//     { src: "~plugins/amplify.js" },
//     "~/plugins/vue-gtag.js",
//     "~/plugins/vue-mq.js",
//   ],
  /*
   ** Nuxt.js modules
   */
  modules: ["@nuxtjs/style-resources", "@nuxtjs/robots", "nuxt-socket-io"],
//   styleResources: {
//     scss: ["~/assets/_media-queries.scss", "~/assets/vuetify-override.scss"],
//   },

  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    extend(config, ctx) {},
  },
  buildModules: [
    "@nuxtjs/tailwindcss",
    "@nuxtjs/vuetify",
    "@nuxtjs/axios",
    "@nuxtjs/proxy",
    "@nuxtjs/sitemap",
	"@nuxtjs/dotenv"
  ],
  vuetify: {
    /* module options */
  },
  io: {
    // module options
    sockets: [
      {
        name: "home",
        // url: "https://api.footlooseai.com:8080",
        url: "http://localhost:8081",
      },
    ],
  },
  axios: {
    // baseURL: "https://api.footlooseai.com:8080",
    baseURL: "http://localhost:8081",
    proxyHeaders: false,
    credentials: false,
  },
//   sitemap: {
//     hostname: "https://footlooseai.com",
//     routes() {
//       return getRoutes();
//     },
//     path: "/sitemap.xml",
//     gzip: true,
//     generate: false,
//   },
};
