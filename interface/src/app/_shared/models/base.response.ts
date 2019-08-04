export class BaseResponse<TModel> {
    public success: boolean;
    public data: TModel;
    public errors: Array<any>;
}