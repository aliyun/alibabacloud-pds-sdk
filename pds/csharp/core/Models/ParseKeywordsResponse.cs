// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * Parse keywords response
     */
    public class ParseKeywordsResponse : TeaModel {
        /// <summary>
        /// AddressLine
        /// </summary>
        [NameInMap("address_line")]
        [Validation(Required=false)]
        public string AddressLine { get; set; }

        [NameInMap("tags")]
        [Validation(Required=false)]
        public List<SystemTag> Tags { get; set; }

        [NameInMap("time_range")]
        [Validation(Required=false)]
        public TimeRange TimeRange { get; set; }

    }

}
