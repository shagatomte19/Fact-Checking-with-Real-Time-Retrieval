import handler from "../pages/api/fact-check";

describe("Fact-Check API", () => {
  it("should return a result for a claim", async () => {
    const mockRequest = {
      method: "POST",
      body: JSON.stringify({ text: "The moon landing was faked" }),
    };
    
    const mockResponse = {
      status: jest.fn().mockReturnThis(),
      json: jest.fn(),
    };

    await handler(mockRequest, mockResponse);

    expect(mockResponse.status).toHaveBeenCalledWith(200);
    expect(mockResponse.json).toHaveBeenCalledWith(expect.objectContaining({
      result: expect.any(Number),
      evidence: expect.any(String),
    }));
  });
});
