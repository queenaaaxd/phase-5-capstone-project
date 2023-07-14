import React from "react";
import ProductList from "./ProductList";
import Search from "./Search";

function ProductPage({ products }) {
    // console.log(products)

    return (
        <main>
            <Search />
            <ProductList products = {products} />
        </main>
    );
}

export default ProductPage;
