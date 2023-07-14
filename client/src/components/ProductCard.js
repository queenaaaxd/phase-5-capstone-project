import React from "react";

function ProductList( {product} ) {
    
    console.log(product.image)

    return (
        <li className="card">
            <img src={product.image} alt={product.name} />
            <h4>{product.name}</h4>
            <p>${product.price}</p>
            <button>ADD TO CART</button>
    </li>
    )
}

export default ProductList;
