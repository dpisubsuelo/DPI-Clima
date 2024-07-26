import { useDispatch, useSelector } from "react-redux";
import { usePostClimaMutation } from '../store/apiSlice';

const Clima = () => {

  const [apiEnviarGrados] = usePostClimaMutation();
  const dispatch = useDispatch()
  
    const manejarCambio = (e) => {
    const { name, value } = e.target;
      dispatch(apiEnviarGrados({ [name]: value }));
    }
  
    const enviar = (e) => {
    e.preventDefault();
    try {
      dispatch(apiAddOrdenTrabajo(formulario));
    } catch {
      console.error();
    };

  }
  
  
  return(
  <>
  <input type="text" name="grados" onChange={manejarCambio} />
  
  </>
)}
export default Clima
