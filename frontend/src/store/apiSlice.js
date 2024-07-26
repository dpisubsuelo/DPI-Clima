import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const objetosApi = createApi({
    reducerPath: "objetosApi",
    baseQuery: fetchBaseQuery({ baseUrl: "http://localhost:8000/" }),
    endpoints: (builder) => ({
        postClima: builder.mutation({
            query: (grados) => ({
                url: "soap/",
                method: "POST",
                body: grados,
            }),
        }),
        GetClima: builder.query({
            query: (grados) => ({
                url: `soap/${grados}`,
                method: "GET",
            }),
        }),
    }),
});

export const { usePostClimaMutation, useGetClimaQuery } = objetosApi;
