import {Example} from 'src/example/service/exampleResponse';

interface IState {
    Example: Example[],
    TxtEmail: string
}

export { IState as State }