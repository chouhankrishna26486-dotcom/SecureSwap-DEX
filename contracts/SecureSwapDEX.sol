State variables
    address public owner;
    uint256 public feePercentage; Events
    event LiquidityAdded(address indexed provider, uint256 amount, uint256 timestamp);
    event LiquidityRemoved(address indexed provider, uint256 amount, uint256 timestamp);
    event TokenSwapped(address indexed user, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);
    event TokenAdded(address indexed token, uint256 timestamp);
    event TokenRemoved(address indexed token, uint256 timestamp);
    event FeeUpdated(uint256 oldFee, uint256 newFee);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    
    0.3% default fee
    }
    
    /**
     * @dev Function 1: Add liquidity to the DEX
     * @param amount Amount of liquidity to add
     */
    function addLiquidity(uint256 amount) external payable {
        require(amount > 0 || msg.value > 0, "Amount must be greater than zero");
        
        uint256 liquidityAmount = amount > 0 ? amount : msg.value;
        liquidityProviders[msg.sender] += liquidityAmount;
        totalLiquidity += liquidityAmount;
        
        emit LiquidityAdded(msg.sender, liquidityAmount, block.timestamp);
    }
    
    /**
     * @dev Function 2: Remove liquidity from the DEX
     * @param amount Amount of liquidity to remove
     */
    function removeLiquidity(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(liquidityProviders[msg.sender] >= amount, "Insufficient liquidity");
        
        liquidityProviders[msg.sender] -= amount;
        totalLiquidity -= amount;
        
        payable(msg.sender).transfer(amount);
        
        emit LiquidityRemoved(msg.sender, amount, block.timestamp);
    }
    
    /**
     * @dev Function 3: Swap tokens with automated pricing
     * @param tokenIn Address of input token
     * @param tokenOut Address of output token
     * @param amountIn Amount of input tokens
     */
    function swapTokens(address tokenIn, address tokenOut, uint256 amountIn) 
        external 
        validToken(tokenIn) 
        validToken(tokenOut) 
    {
        require(amountIn > 0, "Amount must be greater than zero");
        require(userBalances[msg.sender][tokenIn] >= amountIn, "Insufficient balance");
        
        uint256 fee = (amountIn * feePercentage) / 10000;
        uint256 amountAfterFee = amountIn - fee;
        
        Simplified calculation - in production, use proper AMM formula
        return (amountIn * 98) / 100; End
// 
// 
End
// 
