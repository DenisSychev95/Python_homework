import { useState, useEffect } from "react";

function Counter() {

    let [cnt, setCnt] = useState(0);

    let increment = () => setCnt(cnt + 1);
    /* let decrement = () => setCnt(cnt - 1); */

    function decrement() {
        setCnt(cnt - 1)
    };

     useEffect(() => {
        console.log("Hello from counter", cnt);
        return ()=> console.log("Goodbye counter");
                
    }, [cnt])

    return (
        <div>
            <h2>Счетчик: </h2>
            <h1>{cnt}</h1>
            <button onClick={decrement}>- Минус</button>
            <button onClick={increment}>+ Плюс</button>
        </div>
    )
}

export default Counter