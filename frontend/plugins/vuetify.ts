import { createVuetify } from 'vuetify'

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
    ssr: false,
    // ... your configuration
  })
  app.vueApp.use(vuetify)
})
