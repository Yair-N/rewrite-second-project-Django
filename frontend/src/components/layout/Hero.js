import React from 'react'
import styled from 'styled-components'

const Hero = () => {
    return (
        <HeroSection>
            
        </HeroSection>
    )
}

export default Hero

const HeroSection = styled.div`
position:absolute;
display:flex;
flex-direction:column;
top:15vh;
left:50%;
margin:10px 10px 10px 10px;
width:100%;
height:100%;
min-height:400px;
max-height:50vh;
max-width:800px;
background-color:#ffffff;
border-radius:1rem;
transform:translate(-50%);
box-shadow: .1rem .1rem 15px -2px gray;
`