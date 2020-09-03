// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 
     */
    public class ImageQuality : TeaModel {
        [NameInMap("clarity")]
        [Validation(Required=false)]
        public int? Clarity { get; set; }

        [NameInMap("clarity_score")]
        [Validation(Required=false)]
        public int? ClarityScore { get; set; }

        [NameInMap("color")]
        [Validation(Required=false)]
        public int? Color { get; set; }

        [NameInMap("color_score")]
        [Validation(Required=false)]
        public int? ColorScore { get; set; }

        [NameInMap("composition_score")]
        [Validation(Required=false)]
        public int? CompositionScore { get; set; }

        [NameInMap("contrast")]
        [Validation(Required=false)]
        public int? Contrast { get; set; }

        [NameInMap("contrast_score")]
        [Validation(Required=false)]
        public int? ContrastScore { get; set; }

        [NameInMap("exposure")]
        [Validation(Required=false)]
        public int? Exposure { get; set; }

        [NameInMap("exposure_score")]
        [Validation(Required=false)]
        public int? ExposureScore { get; set; }

        [NameInMap("overall_score")]
        [Validation(Required=false)]
        public int? OverallScore { get; set; }

    }

}
