import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders homescreen', () => {
  render(<App />);
  const linkElement = screen.getByText(/Hello!/i);
  expect(linkElement).toBeInTheDocument();
});
