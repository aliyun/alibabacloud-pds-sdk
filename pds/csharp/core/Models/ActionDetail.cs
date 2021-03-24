// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class ActionDetail : TeaModel {
        [NameInMap("create")]
        [Validation(Required=false)]
        public CreateDetail Create { get; set; }

        [NameInMap("delete")]
        [Validation(Required=false)]
        public DeleteDetail Delete { get; set; }

        [NameInMap("edit")]
        [Validation(Required=false)]
        public EditDetail Edit { get; set; }

        [NameInMap("move")]
        [Validation(Required=false)]
        public MoveDetail Move { get; set; }

        [NameInMap("rename")]
        [Validation(Required=false)]
        public RenameDetail Rename { get; set; }

        [NameInMap("restore")]
        [Validation(Required=false)]
        public RestoreDetail Restore { get; set; }

        [NameInMap("trash")]
        [Validation(Required=false)]
        public TrashDetail Trash { get; set; }

    }

}
