import React from "react";
import ProductCard from './ProductCard';

function ProductList({ products }) {
    
    // map
    const productsDisplay = products.map((product) => <ProductCard product={product} key={product.id}/>)

    return (

        <ul className="cards">{productsDisplay}</ul>

    );
}

export default ProductList;
