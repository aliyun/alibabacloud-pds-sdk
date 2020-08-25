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
    public class CroppingBoundary : TeaModel {
        [NameInMap("height")]
        [Validation(Required=false)]
        public long Height { get; set; }

        [NameInMap("left")]
        [Validation(Required=false)]
        public long Left { get; set; }

        [NameInMap("top")]
        [Validation(Required=false)]
        public long Top { get; set; }

        [NameInMap("width")]
        [Validation(Required=false)]
        public long Width { get; set; }

    }

}
