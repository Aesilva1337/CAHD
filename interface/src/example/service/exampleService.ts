import API from '../../shared/api/axiosConfig';
import Urls from 'src/shared/api/urls';
import { AxiosResponse } from 'axios';
import { ExampleResponse } from './exampleResponse';
import ExampleRequest from './exampleRequest';


const ExampleService = {
  getListExample(request: ExampleRequest): Promise<AxiosResponse<ExampleResponse>> {
    debugger;
    return API.get<ExampleResponse>(Urls.ExampleUrl, {
      params: {
        Email: request.email
      }
    });
  }
};

export default ExampleService;
