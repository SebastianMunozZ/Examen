
console.log('hi')

const mostrar = (quecosa) =>{

    let mostrar = 'flex'
    let ocultar = 'none'
    let mostrargato = mostrar
    let mostrarperro = mostrar
    if(quecosa=='Gato'){
        mostrargato = mostrar
        mostrarperro = ocultar
    }else if(quecosa=='Perro'){
        mostrargato = ocultar
        mostrarperro = mostrar
    }

    for(let i=0;i<1000;i++){
        let iddog = `Perro${i}`
        let idcat = `Gato${i}`
        console.log(id)
        try{
            document.getElementById(iddog).style.display = mostrarperro
        }catch{
            //console.log(id, 'don´t exist')
        }
        try{
            document.getElementById(idcat).style.display = mostrargato
        }catch{
            //console.log(id, 'don´t exist')
        }
    }
}

const crudcarro = (tipo,prod)=>{
    if(tipo=='insert'){
        let a = prod.split('_')
        let existe = false
        for(let i=0;i<contenidocarro.length;i++){
            if(a[0]==contenidocarro[i].nombre){
                existe = true
            }
        }
        if(!existe){
            contenidocarro.push({
                nombre:a[0],
                cantidad:1,
                precio_un:parseInt(a[1])
            })
            alert('Producto agregado a carrito')
        }else{
            alert('Producto ya está en el carrito. Si quieres más entra al carrito y modifica la cantidad a comprar')
        }
        //console.log(contenidocarro)
        
    }else if(tipo=='delete'){
        contenidocarro = contenidocarro.filter((a,index)=>{return prod!=index})
        listacard()
    }else if(tipo=='update'){
        contenidocarro = contenidocarro.map((a)=>{if(a.id===prod.id){return prod}else{return a}})
    }else if(tipo=='read'){
        return contenidocarro
    }
}

let contenidocarro = []

const listacard = ()=>{
    console.log('lista!')
    let totalcompra = 0
    let filas = contenidocarro.map((i,u)=>{let total = i.cantidad*i.precio_un;totalcompra+=total;return `
      <tr>
        <th scope="row">${u+1}</th>
        <td>${i.nombre}</td>
        <td id="${u}_cantidad"><div id="${u}_cantidad_un">${i.cantidad}</div><div class="btn-group" role="group" aria-label="Basic example">
        <button onclick="actualizar(${u},-1)" type="button" class="btn btn-primary" style="background-color: #0fb4ac;margin-left: 3px">-</button>
        <button onclick="actualizar(${u},1)" type="button" class="btn btn-primary" style="background-color: #0fb4ac;margin-right: 3px;">+</button>
      </div></td>
        <td id="${u}_precio_u">${i.precio_un}</td>
        <td id="${u}_total">${total}</td>
        <td id="${u}_quitar"><button type="button" class="btn btn-danger" onclick="crudcarro('delete',${u})">Quitar</button></td>
      </tr>
      `})
    filas = filas.join('')
    let body = `<table class="table">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Producto</th>
        <th scope="col">Cantidad</th>
        <th scope="col">Precio</th>
        <th scope="col">Total</th>
      </tr>
    </thead>
    <tbody>
      ${filas}
      <tr>
      <th scope="row"></th>
      <td></td>
      <td></td>
      <td><b>Total</b></td>
      <td id="total_compra" style ="font-weight: bold;">${totalcompra}</td>
    </tr>
    </tbody>
  </table>
  `
    document.getElementById('lista_compra').innerHTML = body
}

const actualizar = (id,valor)=>{

    let value1 = parseInt(document.getElementById(`${id}_cantidad_un`).innerHTML)
    let niucantidad = Math.max(parseInt(valor)+parseInt(value1),1)
    let precio_un = parseInt(document.getElementById(`${id}_precio_u`).innerHTML)
    let precioantiguo = value1*precio_un
    document.getElementById(`${id}_total`).innerHTML = parseInt(precio_un)*niucantidad
    let totalcompra = parseInt(document.getElementById("total_compra").innerHTML)
    contenidocarro[id].cantidad = niucantidad
    //console.log(contenidocarro[id])
    document.getElementById("total_compra").innerHTML = totalcompra + (parseInt(precio_un)*niucantidad) - precioantiguo
    //console.log(value1,niucantidad,precio_un,precioantiguo,totalcompra)
    document.getElementById(`${id}_cantidad`).innerHTML= `<div id="${id}_cantidad_un">${niucantidad}</div> <div class="btn-group" role="group" aria-label="Basic example">
    <button onclick="actualizar(${id},-1)" type="button" class="btn btn-primary" style="background-color: #0fb4ac;margin-left: 3px">-</button>
    <button onclick="actualizar(${id},1)" type="button" class="btn btn-primary" style="background-color: #0fb4ac;margin-right: 3px;">+</button>
  </div>`
}

listacard()
//mostrar('Gato')

