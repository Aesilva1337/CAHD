import { BaseResponse } from 'src/app/_shared/models/base.response';

export class ListarDiagnosticoResponse extends BaseResponse<ListarDiagnosticoModel[]>{
}

export class ListarDiagnosticoModel{
    public idDiagnostico: number;
    public tituloDiagnostico: string;
    public descDiagnostico: string;
}