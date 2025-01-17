
import reactPlugin from 'eslint-plugin-react';
import typescriptPlugin from '@typescript-eslint/eslint-plugin';

export default [
  {
    files: ['**/*.{js,jsx,ts,tsx}'],
    languageOptions: {
ecmaVersion: 'latest',
      sourceType: 'module',

    },
    plugins: {
      react: reactPlugin,
      '@typescript-eslint': typescriptPlugin,
    },
    rules: {
      semi: ['error', 'always'],
      quotes: ['error', 'single'],
      'no-unused-vars': 'warn',
      'react/prop-types': 'off',
    },
  },
];
