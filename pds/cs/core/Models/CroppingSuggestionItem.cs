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
    public class CroppingSuggestionItem : TeaModel {
        [NameInMap("aspect_ratio")]
        [Validation(Required=false)]
        public string AspectRatio { get; set; }

        [NameInMap("cropping_boundary")]
        [Validation(Required=false)]
        public CroppingBoundary CroppingBoundary { get; set; }

        [NameInMap("score")]
        [Validation(Required=false)]
        public double? Score { get; set; }

    }

}
