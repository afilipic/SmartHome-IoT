import { createGlobalStyle } from "styled-components";
import styled from "styled-components";

export const GlobalStyle = createGlobalStyle`
  body {
    margin: 0;
    padding: 0;
    background-color: ${({ theme }) => theme.colors.secondColor};
  }
`;

export const StyledPage = styled.div`
  display: flex;
`;

export const StyledPanel = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center; /* Centriramo dugmadi */
  width:250px;
  height:280px;
  margin-right: 20px; /* Dodajte margine po potrebi */
  position: fixed; /* Fiksiramo panel na ekranu */
  top: 20%; /* Postavljamo panel na vrh ekrana */
  right: 7%; /* Postavljamo panel na desnu stranu ekrana */
  padding: 10px; /* Dodajte padding po potrebi */
  background-color: #213535; /* Tamnozelena boja */
  border-radius: 20px; /* Zaobljene ivice */
  z-index: 1; /* Postavljamo z-index tako da bude iznad ostalog sadržaja */
`;
export const StyledPanel2 = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center; /* Centriramo dugmadi */
  width:250px;
  height:180px;
  margin-right: 20px; /* Dodajte margine po potrebi */
  position: fixed; /* Fiksiramo panel na ekranu */
  top: 61%; /* Postavljamo panel na vrh ekrana */
  right: 7%; /* Postavljamo panel na desnu stranu ekrana */
  padding: 10px; /* Dodajte padding po potrebi */
  background-color: #213535; /* Tamnozelena boja */
  border-radius: 20px; /* Zaobljene ivice */
  z-index: 1; /* Postavljamo z-index tako da bude iznad ostalog sadržaja */
`;
export const StyledButton = styled.button`
  background-color: #b4e854; /* Light green color */
  border: none;
  border-radius: 25px;
  padding: 15px;
  font-size:18px;
  color:#213535;
  margin-top: 12px; /* Add a gap between buttons */
  cursor: pointer;
`;