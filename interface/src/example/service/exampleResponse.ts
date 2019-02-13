import BaseResponse from 'src/shared/api/baseResponse';


class ExampleResponse extends BaseResponse{
    examples: Array<Example>
}

class Example {
    idExample: number;
    email: string;
    name: string;
}

export { ExampleResponse, Example }