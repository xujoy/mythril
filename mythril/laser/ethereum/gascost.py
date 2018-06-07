gascost = {
    'PUSH': 3,
    'DUP': 3,
    'SWAP': 3,
    'STOP': 0,
    'ADD': 3,
    'MUL': 5,
	'SUB': 3,
    'DIV': 5,
    'SDIV': 5,
    'MOD': 5,
    'SMOD': 5,
    'ADDMOD': 8,
    'MULMOD': 8,
    'EXP': 10,
    'SIGNEXTEND': 5,
    'LT': 3,
    'GT': 3,
    'SLT': 3,
    'SGT': 3,
    'EQ': 3,
    'ISZERO': 3,
    'AND': 3,
    'OR': 3,
    'XOR': 3,
    'NOT': 3,
    'BYTE': 3,
    'SHA3': 30,
    'ADDRESS': 2,
    'BALANCE': 400,
    'ORIGIN': 2,
    'CALLER': 2,
    'CALLVALUE': 2,
    'CALLDATALOAD': 3,
    'CALLDATASIZE': 2,
    'CALLDATACOPY': 3,
    'CODESIZE': 2,
    'CODECOPY': 3,
    'GASPRICE': 2,
    'EXTCODESIZE': 700,
    'EXTCODECOPY': 700,
    'BLOCKHASH': 20,
    'COINBASE': 2,
    'TIMESTAMP': 2,
    'NUMBER': 2,
    'DIFFICULTY': 2,
    'GASLIMIT': 2,
    'POP': 2,
    'MLOAD': 3,
    'MSTORE': 3,
    'MSTORE8': 3,
    'SLOAD': 50,
    'SSTORE': 0,
    'JUMP': 8,
    'JUMPI': 10,
    'PC': 2,
    'MSIZE': 2,
    'GAS': 2,
    'JUMPDEST': 1,
    'LOG0': 375,
    'LOG1': 750,
    'LOG2': 1125,
    'LOG3': 1500,
    'LOG4': 1875,
    'CREATE': 32000,
    'CALL': 40,
    'CALLCODE': 40,
    'RETURN': 0,
    'DELEGATECALL': 40,
    'CALLBLACKBOX': 40,
    'STATICCALL': 40,
    'REVERT': 0,
    'SUICIDE': 5000,
}