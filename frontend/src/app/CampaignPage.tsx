import React, { FormEvent, useState, useEffect } from "react";
import Table from 'react-bootstrap/Table';


export default function CampaignPage() {
  const [products, setProducts] = useState([]);
  const [campaigns, setCampaigns] = useState([]);
  const [productResults, setProductResult] = useState('');
  const [campaignResults, setCampaignResult] = useState('');

  useEffect(() => {
    getProducts()
    getCampaigns()
  }, [])

  const getProducts = async () => {
    let productsResponse = await fetch('http://0.0.0.0:8000/api/products/',
      {
        headers: {
          'Content-Type': 'application/json'
        },
        method: 'GET',
      }
    )
    let json = await productsResponse.json();
    setProducts(json.results)
  }

  const getCampaigns = async () => {
    let campaignsResponse = await fetch('http://0.0.0.0:8000/api/campaigns/',
      {
        headers: {
          'Content-Type': 'application/json'
        },
        method: 'GET',
      }
    )
    let json = await campaignsResponse.json();
    setCampaigns(json.results)
  }

  const sendCampaignForm = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault()
  
    const { name, product_id, start_date, end_date } = event.target as typeof event.target & {
      name: { value: string}
      product_id: { value: string}
      start_date: { value: string}
      end_date: { value: string}
    }
  
    const resp = await fetch('http://0.0.0.0:8000/api/campaigns/', 
      {
        headers: {
          'Content-Type': 'application/json'
      },
      method: 'POST',
      body: JSON.stringify({
        name: name.value,
        product: {id: product_id.value},
        start_date: start_date.value,
        end_date: end_date.value
      })
    })

    let json = await resp.json();
    setCampaignResult(JSON.stringify(json))
    getCampaigns()
  }


  const sendProductForm = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault()
  
    const { name } = event.target as typeof event.target & {
      name: { value: string}
    }
  
    const resp = await fetch('http://0.0.0.0:8000/api/products/', 
      {
        headers: {
          'Content-Type': 'application/json'
      },
      method: 'POST',
      body: JSON.stringify({
        name: name.value
      })
    })

    let json = await resp.json();
    setProductResult(JSON.stringify(json))
    getProducts()
  }


  return (
    <div>
      <h1>Products</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>NAME</th>
          </tr>
        </thead>
        <tbody>
          {products.map((data) => {return(<tr><td>{data.id}</td><td>{data.name}</td></tr>)})}
        </tbody>
      </Table>
      <h1>Submit Product</h1>
      <form className="wrap" onSubmit={evt => { sendProductForm(evt) }}>
        <fieldset>
          <label htmlFor="name">NAME:</label>
          <input type="text" id="name" />
        </fieldset>
        <button type="submit">Submit</button>
      </form>
      <p>
        {productResults}
      </p>
      <br></br>
      <h1>Campaigns</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>NAME</th>
            <th>PRODUCT</th>
            <th>START_DATE</th>
            <th>END_DATE</th>
            <th>IS_ACTIVE</th>
          </tr>
        </thead>
        <tbody>
          {campaigns.map((data) => {
              return(
                <tr>
                  <td>{data.id}</td>
                  <td>{data.name}</td>
                  <td>{data.product.name}</td>
                  <td>{data.start_date}</td>
                  <td>{data.end_date}</td>
                  <td>{data.is_active + ''}</td>
                </tr>)
            })
          }
        </tbody>
      </Table>
      <h1>Submit Campaign</h1>
      <form className="wrap" onSubmit={evt => { sendCampaignForm(evt) }}>
        <fieldset>
          <label htmlFor="name">NAME:</label>
          <input type="text" id="name" />
        </fieldset>
        <fieldset>
          <label htmlFor="product_id">PRODUCT ID:</label>
          <input type="product_id" id="product_id" />
        </fieldset>
        <fieldset>
          <label htmlFor="start_date">START DATE:</label>
          <input type="start_date" id="start_date" />
        </fieldset>
        <fieldset>
          <label htmlFor="end_date">END DATE:</label>
          <input type="end_date" id="end_date" />
        </fieldset>
        <button type="submit">Submit</button>
      </form>
      <p>
        {campaignResults}
      </p>
    </div>
  )
}
