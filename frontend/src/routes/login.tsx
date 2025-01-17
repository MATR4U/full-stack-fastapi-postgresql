import { ViewIcon, ViewOffIcon } from '@chakra-ui/icons';
import {
  Button,
  Center,
  Container,
  FormControl,
  FormErrorMessage,
  Icon,
  Image,
  Input,
  InputGroup,
  InputRightElement,
  Link,
  useBoolean,
} from '@chakra-ui/react';
import {
  Link as RouterLink,
  createFileRoute,
  redirect,
} from '@tanstack/react-router';
import { type SubmitHandler, useForm } from 'react-hook-form';

import Logo from '/assets/images/fastapi-logo.svg';
import type { Body_login_login_access_token as AccessToken } from '../client';
import useAuth, { isLoggedIn } from '../hooks/useAuth';
import { emailPattern } from '../utils';

// Define the login route
export const Route = createFileRoute('/login')({
  component: Login,
  beforeLoad: async () => {
    // Redirect to home if the user is already logged in
    if (isLoggedIn()) {
      throw redirect({
        to: '/',
      });
    }
  },
});

function Login() {
  // State to toggle password visibility
  const [show, setShow] = useBoolean();
  
  // State for error message
  const [errorMessage, setErrorMessage] = useState('');

  // Authentication hooks
  const { loginMutation, error, resetError } = useAuth();

  // Form handling with react-hook-form
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<AccessToken>({
    mode: 'onBlur',
    criteriaMode: 'all',
    defaultValues: {
      username: '',
      password: '',
    },
  });

  // Handle form submission
const onSubmit: SubmitHandler<AccessToken> = async (data) => {
    if (isSubmitting) return;

    resetError();

    try {
      await loginMutation.mutateAsync(data);
    } catch (err) {
      console.error('Login failed:', err);
      setError('Login failed. Please try again.');
    }
  };

  return (
    <>
      {/* Form container */}
      <Container
        as="form"
        onSubmit={handleSubmit(onSubmit)}
        h="100vh"
        maxW="sm"
        alignItems="stretch"
        justifyContent="center"
        gap={4}
        centerContent
      >
        {/* Logo */}
        <Image
          src={Logo}
          alt="FastAPI logo"
          height="auto"
          maxW="2xs"
          alignSelf="center"
          mb={4}
        />
        {/* Username input */}
        <FormControl id="username" isInvalid={!!errors.username || !!error}>
          <Input
            id="username"
            {...register('username', {
              pattern: emailPattern,
            })}
            placeholder="Email"
            type="email"
            required
          />
          {errors.username && (
            <FormErrorMessage>{errors.username.message}</FormErrorMessage>
          )}
        </FormControl>
        {/* Password input */}
        <FormControl id="password" isInvalid={!!error}>
          <InputGroup>
            <Input
              {...register('password')}
              type={show ? 'text' : 'password'}
              placeholder="Password"
              required
            />
            <InputRightElement
              color="ui.dim"
              _hover={{
                cursor: 'pointer',
              }}
            >
              <Icon
                onClick={setShow.toggle}
                aria-label={show ? 'Hide password' : 'Show password'}
              >
                {show ? <ViewOffIcon /> : <ViewIcon />}
              </Icon>
            </InputRightElement>
          </InputGroup>
{error && <FormErrorMessage>{error}</FormErrorMessage>}
          {errorMessage && <FormErrorMessage>{errorMessage}</FormErrorMessage>}
        </FormControl>
        {/* Forgot password link */}
        <Center>
          <Link as={RouterLink} to="/recover-password" color="blue.500">
            Forgot password?
          </Link>
        </Center>

        {/* Submit button */}
        <Button variant="primary" type="submit" isLoading={isSubmitting}>
          Log In
        </Button>
      </Container>
    </>
  );
}
