import React, {useState} from "react";
import ProductList from "./ProductList";
import Search from "./Search";

function ProductPage({ products, addToCart }) {

    const [search, setSearch] = useState("");

    // const searchList = products.filter(([product]) => {
    //     return product.name.toLowerCase().includes(search.toLowerCase());
    // })

    // console.log(products)

    return (
        <main>
            <Search search={ search } setSearch={ setSearch } />
            <ProductList products = {products} addToCart= {addToCart} />
        </main>
    );
}

export default ProductPage;
