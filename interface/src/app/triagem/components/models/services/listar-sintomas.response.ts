import { BaseResponse } from 'src/app/_shared/models/base.response';

export class ListarSintomasResponse extends BaseResponse<ListarSintomasModel[]>{
}

export class ListarSintomasModel{
    public idSintoma: number;
    public descricaoSintoma: string;
}