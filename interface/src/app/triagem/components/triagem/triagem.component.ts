import { Component, OnInit } from '@angular/core';
import { TriagemService } from '../services/triagem.service';
import { DiagnosticoModel } from '../models/components/diagnostico.model';

@Component({
    selector: 'app-triagem',
    templateUrl: './triagem.component.html',
    styleUrls: ['./triagem.component.scss']
  })
  export class TriagemComponent implements OnInit {
    constructor(
      private triagemService: TriagemService,
    ) {
    }

    public listDiagnostico: DiagnosticoModel[] = [];

    async ngOnInit() {
      const response = await this.triagemService.ListarDiagnostico();
      response.data.forEach(diag => this.listDiagnostico.push({
        id: diag.idDiagnostico,
        titulo: diag.tituloDiagnostico
      }));
    }

  }