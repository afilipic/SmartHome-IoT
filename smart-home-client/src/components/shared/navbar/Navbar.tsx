import { useEffect, useRef, useState } from "react";
import {
  NavbarStyle,
  Title,
  Menu,
  MenuItem,
  MenuLink,
  Hamburger,
} from "./Navbar.styled";
import { Link } from "react-router-dom";

export interface NavbarProps {
  title: string;
  label?: string;
  isMenuOpen: boolean;
  options: { href: string; value: string }[];
  footerRef?: React.RefObject<HTMLDivElement>;
  setIsMenuOpen: React.Dispatch<React.SetStateAction<boolean>>;
}

export default function Navbar({
  title,
  isMenuOpen,
  setIsMenuOpen,
  options,
  footerRef,
}: NavbarProps) {



  return (
    <>
      <NavbarStyle>
        <Title as={Link} to={"/"}>
          {title}
        </Title>
        <Hamburger onClick={() => setIsMenuOpen(!isMenuOpen)}>☰</Hamburger>
        <Menu isOpen={isMenuOpen}>
          {options.map((link, index) => (
            <MenuItem key={index}>
              <MenuLink
                as={Link}
                
                to={link.href}
              >
                {link.value}
              </MenuLink>
            </MenuItem>
          ))}
        </Menu>
      </NavbarStyle>
      
    </>
  );
}
