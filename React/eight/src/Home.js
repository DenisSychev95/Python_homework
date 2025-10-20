import { useState } from "react";
import Goods from "./components/goods/Goods";
import Total from "./components/Total";

function Home() {
    const goods = [{ id: "1", product: "Apple", isChecked: false }, { id: "2", product: "Banana", isChecked: false }, { id: "3", product: "Tea", isChecked: false }, { id: "4", product: "Coffee", isChecked: false }];
    const [count, setCount] = useState([]);
    /* const [visible, setVisible] = useState(false); */


    /*     const changeVisible = () => {
            count.length ? setVisible(true) : setVisible(true)
        } */

    const onChangeCount = (id) => {
        if (count.includes(id)) {

            setCount((list) => list.filter((elem) => elem !== id));
        }
        else {
            setCount((list) => [...list, id])
        }
    }

    return (
        <div>
            <h2>Home Page</h2>
            <h3>Shopping list:</h3>
            <Goods
                goods={goods}
                onChangeCount={onChangeCount}

            />
            {count.length > 0 && < Total res={count.length} /> }

        </div>
    )
}

export default Home;