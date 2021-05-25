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
    public class ImageQuality : TeaModel {
        [NameInMap("clarity")]
        [Validation(Required=false)]
        public double? Clarity { get; set; }

        [NameInMap("clarity_score")]
        [Validation(Required=false)]
        public double? ClarityScore { get; set; }

        [NameInMap("color")]
        [Validation(Required=false)]
        public double? Color { get; set; }

        [NameInMap("color_score")]
        [Validation(Required=false)]
        public double? ColorScore { get; set; }

        [NameInMap("composition_score")]
        [Validation(Required=false)]
        public double? CompositionScore { get; set; }

        [NameInMap("contrast")]
        [Validation(Required=false)]
        public double? Contrast { get; set; }

        [NameInMap("contrast_score")]
        [Validation(Required=false)]
        public double? ContrastScore { get; set; }

        [NameInMap("exposure")]
        [Validation(Required=false)]
        public double? Exposure { get; set; }

        [NameInMap("exposure_score")]
        [Validation(Required=false)]
        public double? ExposureScore { get; set; }

        [NameInMap("overall_score")]
        [Validation(Required=false)]
        public double? OverallScore { get; set; }

    }

}
