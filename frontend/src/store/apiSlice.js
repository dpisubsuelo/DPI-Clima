import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const objetosApi = createApi({
    reducerPath: "objetosApi",
    baseQuery: fetchBaseQuery({ baseUrl: "http://localhost:8000/" }),
    endpoints: (builder) => ({

        postClima: builder.mutation({
            query: (grados) => ({
                url: "desdesoap",
                method: "POST",
                body: grados,
            }),
        }),


    })
});

export const { usePostClimaMutation } = objetosApi;