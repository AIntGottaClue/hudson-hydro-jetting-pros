import { defineConfig } from 'astro/config';
export default defineConfig({base:process.env.BASE ?? "/",site:'https://hudsonhydrojetting.prosapp.site',trailingSlash:'always',build:{format:'directory'}});
