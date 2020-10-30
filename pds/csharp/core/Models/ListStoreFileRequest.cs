// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * list store file
     */
    public class ListStoreFileRequest : TeaModel {
        /// <summary>
        /// limit
        /// </summary>
        [NameInMap("limit")]
        [Validation(Required=false)]
        public long? Limit { get; set; }

        /// <summary>
        /// marker
        /// </summary>
        [NameInMap("marker")]
        [Validation(Required=false)]
        public string Marker { get; set; }

        /// <summary>
        /// parent_file_path
        /// </summary>
        [NameInMap("parent_file_path")]
        [Validation(Required=false)]
        public string ParentFilePath { get; set; }

        /// <summary>
        /// store_id
        /// </summary>
        [NameInMap("store_id")]
        [Validation(Required=false)]
        public string StoreId { get; set; }

        /// <summary>
        /// type
        /// </summary>
        [NameInMap("type")]
        [Validation(Required=false)]
        public string Type { get; set; }

    }

}
