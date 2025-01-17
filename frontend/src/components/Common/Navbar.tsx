import { Button, Flex, Icon, useDisclosure } from '@chakra-ui/react';
import { FaPlus } from 'react-icons/fa';

import AddUser from '../Admin/AddUser/AddUser';
import AddItem from '../Items/AddItem';

interface NavbarProps {
  type: string;
}

// Navbar component
const Navbar = ({ type }: NavbarProps) => {
  const addUserModal = useDisclosure();
  const addItemModal = useDisclosure();

  // Handle button click based on type
  const handleButtonClick = () => {
    if (type === 'User') {
      addUserModal.onOpen();
    } else {
      addItemModal.onOpen();
    }
  };

  return (
    <>
      <Flex py={8} gap={4}>
        {/* TODO: Complete search functionality */}
        {/* <InputGroup w={{ base: '100%', md: 'auto' }}>
                    <InputLeftElement pointerEvents='none'>
                        <Icon as={FaSearch} color='ui.dim' />
                    </InputLeftElement>
                    <Input type='text' placeholder='Search' fontSize={{ base: 'sm', md: 'inherit' }} borderRadius='8px' />
                </InputGroup> */}
        <Button
          variant="primary"
          gap={1}
          fontSize={{ base: 'sm', md: 'inherit' }}
          onClick={handleButtonClick}
        >
          <Icon as={FaPlus} /> Add {type}
        </Button>
        <AddUser isOpen={addUserModal.isOpen} onClose={addUserModal.onClose} />
        <AddItem isOpen={addItemModal.isOpen} onClose={addItemModal.onClose} />
      </Flex>
    </>
  );
};

export default Navbar;
