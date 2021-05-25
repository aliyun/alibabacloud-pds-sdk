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
    public class SystemTag : TeaModel {
        [NameInMap("confidence")]
        [Validation(Required=false)]
        public double? Confidence { get; set; }

        [NameInMap("en_name")]
        [Validation(Required=false)]
        public string EnName { get; set; }

        [NameInMap("name")]
        [Validation(Required=false)]
        public string Name { get; set; }

        [NameInMap("parent_en_name")]
        [Validation(Required=false)]
        public string ParentEnName { get; set; }

        [NameInMap("parent_name")]
        [Validation(Required=false)]
        public string ParentName { get; set; }

        [NameInMap("selected")]
        [Validation(Required=false)]
        public bool? Selected { get; set; }

        [NameInMap("source")]
        [Validation(Required=false)]
        public string Source { get; set; }

        [NameInMap("tag_level")]
        [Validation(Required=false)]
        public long? TagLevel { get; set; }

    }

}
