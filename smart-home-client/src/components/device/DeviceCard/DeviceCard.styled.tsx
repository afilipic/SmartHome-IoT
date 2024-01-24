// DeviceCard.styled.ts
import styled from "styled-components";

export const Card = styled.article`
  width: 100px;
  height: 100px;
  padding: 20px;
  position: relative;
  margin: 20px;
  text-align: center;
  border-radius: 50%;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(to bottom, #b4e854, #699a1e); /* Gradient from lighter to darker green */

  h3 {
    margin: 0;
    color: white;
    font-size: 20px;
  }

  &:hover {
    transform: scale(1.1);
    cursor: pointer;
  }

  transition: transform 0.3s ease-in-out;
`;
