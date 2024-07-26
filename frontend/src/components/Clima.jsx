import { useDispatch, useSelector } from "react-redux";
import { usePostClimaMutation, useGetClimaQuery } from "../store/apiSlice";
import { useState } from "react";

const Clima = () => {
    const [formulario, setFormulario] = useState("");
    const [grados, setGrados] = useState("0");
    const [apiEnviarGrados] = usePostClimaMutation();
    const dispatch = useDispatch();

    const manejarCambio = (e) => {
        const { value } = e.target;
        setFormulario(value);
        // console.log(formulario);
        // dispatch(apiEnviarGrados({ [name]: value }));
    };
    const { data, error, isError, isLoading } = useGetClimaQuery(grados);
    console.log(data);

    const enviar = (e) => {
        console.log(formulario);
        setGrados(formulario);
        // e.preventDefault();
        // try {
        //     dispatch(apiEnviarGrados(formulario));
        // } catch {
        //     console.error();
        // }
    };

    if (isLoading) return <div>Cargando</div>;
    // else if (data) return <div>Con datos</div>;
    else if (isError) return <div>Error: {error.message}</div>;

    return (
        <>
            <input
                type="text"
                name="grados"
                value={formulario.grados}
                onChange={manejarCambio}
            />
            <button onClick={enviar}>Enviar</button>
            {isLoading && <p>Cargando...</p>}
            {error && <p>Error</p>}
            {data && grados !== "0" && <p>{data}</p>}
        </>
    );
};
export default Clima;
