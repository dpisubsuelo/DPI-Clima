import { configureStore } from "@reduxjs/toolkit";

import { objetosApi } from "./apiSlice";

export const store = configureStore({
    reducer: {

        [objetosApi.reducerPath]: objetosApi.reducer
    },
    middleware: (getDefaultMiddleware) =>
            getDefaultMiddleware().concat(objetosApi.middleware)
})