<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * list_file_by_anonymous request.
 */
class ListByAnonymousRequest extends Model
{
    public $headers;

    /**
     * @description limit
     *
     * @example 50
     *
     * @var int
     */
    public $limit;

    /**
     * @description marker
     *
     * @example NWQ1Yjk4YmI1ZDRlYmU1Y2E0YWE0NmJhYWJmODBhNDQ2NzhlMTRhMg
     *
     * @var string
     */
    public $marker;

    /**
     * @description parent_file_id
     *
     * @example root
     *
     * @var string
     */
    public $parentFileId;

    /**
     * @description share_id
     *
     * @example z6e81Up4u3GDBoJ741dm8z8fZBc2dh8gW
     *
     * @var string
     */
    public $shareId;
    protected $_name = [
        'limit'        => 'limit',
        'marker'       => 'marker',
        'parentFileId' => 'parent_file_id',
        'shareId'      => 'share_id',
    ];

    public function validate()
    {
        Model::validateMaximum('limit', $this->limit, 100);
        Model::validateMinimum('limit', $this->limit, 1);
        Model::validateRequired('parentFileId', $this->parentFileId, true);
        Model::validateRequired('shareId', $this->shareId, true);
        Model::validateMaxLength('parentFileId', $this->parentFileId, 50);
        Model::validateMinLength('parentFileId', $this->parentFileId, 4);
        Model::validatePattern('parentFileId', $this->parentFileId, '[a-z0-9]{1,50}');
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->limit) {
            $res['limit'] = $this->limit;
        }
        if (null !== $this->marker) {
            $res['marker'] = $this->marker;
        }
        if (null !== $this->parentFileId) {
            $res['parent_file_id'] = $this->parentFileId;
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ListByAnonymousRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['limit'])) {
            $model->limit = $map['limit'];
        }
        if (isset($map['marker'])) {
            $model->marker = $map['marker'];
        }
        if (isset($map['parent_file_id'])) {
            $model->parentFileId = $map['parent_file_id'];
        }
        if (isset($map['share_id'])) {
            $model->shareId = $map['share_id'];
        }

        return $model;
    }
}
