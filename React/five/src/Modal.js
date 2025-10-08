import { useState } from "react";
import "./Modal.css"

function Modal() {

    let image = "https://cdn.shazoo.ru/98318_7HnrBDM4Xz_1419874968_witcher_3_steelbook_n.jpg"
    let [open, setOpen] = useState(false)

    return (
        <div>
            <img src={image} className='small' alt="" onClick={() => setOpen(true)} style={{ display: open ? "none" : "block" }} />


            {open && (<div>
                <div>
                    <img src={image} className="big" alt="Portret" onClick={()=> setOpen(false)}/>
                </div>
            </div>)}
            

        </div>
    )
}

export default Modal