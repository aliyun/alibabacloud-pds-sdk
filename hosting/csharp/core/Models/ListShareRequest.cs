// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * list share request
     */
    public class ListShareRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// creator
        /// </summary>
        [NameInMap("creator")]
        [Validation(Required=false)]
        public string Creator { get; set; }

        [NameInMap("drive_id")]
        [Validation(Required=false, Pattern="[0-9]+")]
        public string DriveId { get; set; }

        /// <summary>
        /// limit
        /// </summary>
        [NameInMap("limit")]
        [Validation(Required=false)]
        public int? Limit { get; set; }

        /// <summary>
        /// marker
        /// </summary>
        [NameInMap("marker")]
        [Validation(Required=false)]
        public string Marker { get; set; }

        /// <summary>
        /// Owner
        /// </summary>
        [NameInMap("owner")]
        [Validation(Required=false)]
        public string Owner { get; set; }

        /// <summary>
        /// owner_type
        /// </summary>
        [NameInMap("owner_type")]
        [Validation(Required=false)]
        public string OwnerType { get; set; }

        /// <summary>
        /// share_file_path
        /// </summary>
        [NameInMap("share_file_path")]
        [Validation(Required=false)]
        public string ShareFilePath { get; set; }

    }

}
