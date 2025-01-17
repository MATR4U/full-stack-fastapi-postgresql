import React from 'react';
import { render, screen } from '@testing-library/react';
import Navbar from './Navbar';

test('renders Navbar component', () => {
  render(<Navbar />);
  const navbarElement = screen.getByRole('navigation');
  expect(navbarElement).toBeInTheDocument();
});
