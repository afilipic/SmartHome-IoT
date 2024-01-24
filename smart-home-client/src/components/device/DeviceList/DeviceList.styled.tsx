// DeviceList.styled.ts
import styled from "styled-components";

export const ItemsListStyle = styled.div`
  /* Dodajte stilove za ItemsListStyle prema vašim potrebama */
`;

export const CircleContainer = styled.div`
  position: relative;
  width: 100%;
  height: 650px;
`;

export const InnerCircle = styled.div`
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;

  h3 {
    margin: 0;
    color: white;
    font-size: 32px; /* Prilagodite veličinu fonta prema potrebama */
  }
`;
