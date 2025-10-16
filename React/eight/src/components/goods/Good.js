import { useState } from "react";


function Good({ id, product, isChecked, onChangeCount }) {
    const [checkedElem, setCheckedElem] = useState(isChecked);


    return (
        <div className="inner-li" style={{ color: checkedElem ? "blue" : "", fontSize: checkedElem ? "18px" : "" }}>

            <li><input type="checkbox" id={"inp" + id} onChange={() => {
                setCheckedElem(!checkedElem);
                onChangeCount(id)


            }

            } /><label htmlFor={"inp" + id}>{product}</label></li><span>{checkedElem ? "+" : "-"}</span>


        </div>
    )
}

export default Good;