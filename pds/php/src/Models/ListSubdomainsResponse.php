<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class ListSubdomainsResponse extends Model
{
    /**
     * @description 分页的 subdomain 数据
     *
     * @var BaseSubdomainResponse[]
     */
    public $items;

    /**
     * @description 分页游标，可以用作下次list的起点
     *
     * @example "OGZlODBmMWQtM2RiMi00MjA1LTg2NDktY2NkOThkMmI5NmE5"
     *
     * @var string
     */
    public $nextMarker;
    protected $_name = [
        'items'      => 'items',
        'nextMarker' => 'next_marker',
    ];

    public function validate()
    {
        Model::validateRequired('items', $this->items, true);
        Model::validateRequired('nextMarker', $this->nextMarker, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->items) {
            $res['items'] = [];
            if (null !== $this->items && \is_array($this->items)) {
                $n = 0;
                foreach ($this->items as $item) {
                    $res['items'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->nextMarker) {
            $res['next_marker'] = $this->nextMarker;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ListSubdomainsResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['items'])) {
            if (!empty($map['items'])) {
                $model->items = [];
                $n            = 0;
                foreach ($map['items'] as $item) {
                    $model->items[$n++] = null !== $item ? BaseSubdomainResponse::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['next_marker'])) {
            $model->nextMarker = $map['next_marker'];
        }

        return $model;
    }
}
